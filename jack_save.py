import sys
import signal
import os
import jack
import threading
import struct
import numpy as np



client = jack.Client('Recorder')
client.inports.register('input')

event = threading.Event()

res = []

@client.set_process_callback
def process(frames):
    # breakpoint()
    samples = struct.unpack('f' * client.blocksize, client.inports[0].get_buffer())
    res.extend(samples)


@client.set_shutdown_callback
def shutdown(status, reason):
    print('JACK shutdown!')
    print('status:', status)
    print('reason:', reason)
    event.set()


with client:
    # When entering this with-statement, client.activate() is called.
    # This tells the JACK server that we are ready to roll.
    # Our process() callback will start running now.

    # Connect the ports.  You can't do this before the client is activated,
    # because we can't make connections to clients that aren't running.
    # Note the confusing (but necessary) orientation of the driver backend
    # ports: playback ports are "input" to the backend, and capture ports
    # are "output" from it.

    # capture = client.get_ports(is_physical=True, is_output=True)
    capture = client.get_port_by_name('PulseAudio JACK Sink:front-right')
    client.connect(capture, client.inports[0])

    # playback = client.get_ports(is_physical=True, is_input=True)
    # if not playback:
    #     raise RuntimeError('No physical playback ports')

    # for src, dest in zip(client.outports, playback):
    #     client.connect(src, dest)

    print('Press Ctrl+C to stop')
    try:
        event.wait()
    except KeyboardInterrupt:
        print('\nInterrupted by user')
        np.save("samples.npy", res)

# When the above with-statement is left (either because the end of the
# code block is reached, or because an exception was raised inside),
# client.deactivate() and client.close() are called automatically.