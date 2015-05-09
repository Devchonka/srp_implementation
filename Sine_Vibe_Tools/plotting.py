"""
Plotting module for acoustics analysis

"""

import matplotlib.pyplot as plt


def make_plots(data_df):
    # Figure (1) : Battery Panels
    ax = data_df.plot(y=list(range(3)), title='Sine Accelerometer Overtests', loglog=True)

    plt.xlim([5, 110])
    fig = ax.get_figure()
    fig.suptitle('NBN co 1-A : Battery Panels', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration ([g])', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig1.pdf', bbox_inches='tight')

    # Figure (2) : Solar Array
    ax = data_df.plot(y=[3], title='Sine Accelerometer Overtests', loglog=True)
    plt.xlim([5, 110])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Lower N Solar Array', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration ([g])', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig2.pdf', bbox_inches='tight')

    # Figure (3) : NW Reflector Mid Boom
    ax = data_df.plot(y=[4], title='Sine Accelerometer Overtests', loglog=True)
    plt.xlim([5, 110])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : NW Reflector Boom', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration ([g])', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig3.pdf', bbox_inches='tight')

    # Figure (4) : Tower Earth Sensor
    ax = data_df.plot(y=[5], title='Sine Accelerometer Overtests', loglog=True)
    plt.xlim([5, 110])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Tower Earth Sensor', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration ([g])', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig4.pdf', bbox_inches='tight')

    # Figure (5) : Feed Array
    ax = data_df.plot(y=[6], title='Sine Accelerometer Overtests', loglog=True)
    plt.xlim([5, 110])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : SE Feed Array', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration ([g])', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig5.pdf', bbox_inches='tight')

    # Figure (6) : ECASS
    ax = data_df.plot(y=list(range(7,9)), title='Sine Accelerometer Overtests', loglog=True)

    plt.xlim([5, 110])
    fig = ax.get_figure()
    fig.suptitle('NBN co 1-A : Tower W ECASS', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration ([g])', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig6.pdf', bbox_inches='tight')

    # Figure (2) : LNA Panel
    ax = data_df.plot(y=[9], title='Sine Accelerometer Overtests', loglog=True)
    plt.xlim([5, 110])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : SW LNA Panel', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration ([g])', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig7.pdf', bbox_inches='tight')