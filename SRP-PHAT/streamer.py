import time

from labjack import ljm
import numpy

LABJACK_CLOCK_FREQ = 80.0*10**6
LABJACK_CORE_CLOCK_FREQ = 40.0*10**6
LABJACK_TOP_16_BIT_NAME = 'STREAM_DATA_CAPTURE_16'
SCAN_TIME_KEY = 'system_time'

def write_labjack_commands(labjack_handle, command_list):
  """Helper function to write a list of commands to the labjack."""
  names, values = zip(*command_list)
  ljm.eWriteNames(labjack_handle, len(command_list), names, values)


def chunks(l, n):
  """Yield successive n-sized chunks from l."""
  for i in xrange(0, len(l), n):
    yield l[i:i+n]


def split_by_positions(data, num_positions):
  results = list()
  for i in range(num_positions):
    results.append(data[i::num_positions])
  return results


def reset_labjack(labjack_handle):
  value = int('0x4C4A0001', 0)
  write_labjack_commands(labjack_handle, [('SYSTEM_REBOOT', value)])


class LabjackAnalogReader(object):
  def __init__(self, analog_ports, scan_rate, scans_per_read=None):
    for analog_port in analog_ports:
      assert(0 <= analog_port <= 13)
      assert(int(analog_port) == analog_port)
    if scans_per_read is None:
      scans_per_read = scan_rate / 2.0
    self._scan_rate = int(scan_rate)
    self._scans_per_read = int(scans_per_read)
    self._scan_names = ['AIN' + str(int(port)) for port in analog_ports]
    self._scan_addresses = ljm.namesToAddresses(
        len(self._scan_names), self._scan_names)[0]
    self._init_commands = [(name + '_RANGE', 10) for name in self._scan_names]
    self._init_commands.extend([(name + '_NEGATIVE_CH', 199) for name in self._scan_names])
    self._init_commands.extend([(name + '_RESOLUTION_INDEX', 8) for name in self._scan_names])

  def get_data(self):
    len_ljm_backlog = float('inf')
    len_raw_data = 0
    concat_data = numpy.array([])
    while len_ljm_backlog > len_raw_data:
      raw_data, len_labjack_backlog, len_ljm_backlog = ljm.eStreamRead(self._labjack_handle)
      len_raw_data = len(raw_data)
    return split_by_positions(raw_data, len(self._scan_names))


  def open(self):
    self._labjack_handle = ljm.openS('ANY', 'ANY', 'ANY')
    reset_labjack(self._labjack_handle)
    time.sleep(4)
    write_labjack_commands(self._labjack_handle, self._init_commands)
    ljm.eStreamStart(self._labjack_handle, self._scans_per_read,
                     len(self._scan_names), self._scan_addresses,
                     self._scan_rate)

  def close(self):
    ljm.eStreamStop(self._labjack_handle)
    ljm.close(self._labjack_handle)


def main():
  reader = LabjackAnalogReader([0, 1, 2, 3, 4], 19000)
  reader.open()
  for i in range(50):
    start_time = time.time()
    data = reader.get_data()
    print(time.time() - start_time)
  reader.close()


if __name__ == '__main__':
  main()