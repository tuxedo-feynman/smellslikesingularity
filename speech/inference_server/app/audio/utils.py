import io

import librosa
from path import Path
from pydub import AudioSegment


def _convert_format(audiofile):
    raw_audio = AudioSegment.from_file(audiofile)
    buf = io.BytesIO()
    raw_audio.export(buf, format='flac')
    return buf.getvalue()


def save_to_specto(audiofile):
    specto_filename = Path(MEDIA_ROOT, 'spectos', audiofile.file.stem, 'jpg')

    # convert to flac file
    audiofile = _convert_format(audiofile)
    # Loading the image with no sample rate to use the original sample rate and
    # kaiser_fast to make the speed faster according to a blog post about it (on references)
    X, sample_rate = librosa.load(audiofile, sr=None, res_type='kaiser_fast')
    # Setting the size of the image
    fig = plt.figure(figsize=[1,1])

    # This is to get rid of the axes and only get the picture
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)

    # This is the melspectrogram from the decibels with a linear relationship
    # Setting min and max frequency to account for human voice frequency
    S = librosa.feature.melspectrogram(y=X, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max), x_axis='time', y_axis='mel', fmin=50, fmax=280)

    # Here we finally save the image file choosing the resolution
    plt.savefig(specto_filename, dpi=500, bbox_inches='tight',pad_inches=0)

    # Here we close the image because otherwise we get a warning saying that the image stays
    # open and consumes memory
    plt.close()
    return specto_filename

