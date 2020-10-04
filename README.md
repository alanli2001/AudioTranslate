# AudioTranslate

This application transcribes your audio and translates it to a language of your choice. If you are
deaf/hard of hearing or the speaker is speaking in a different language, this application will
take care of your needs. Built for IvyHacks 2020.

![](https://github.com/alanli2001/ZoomTranslate/blob/main/ZoomTranslate.png)

## To run this program:

1. Clone this repository.
2. You're going to need to set up a [gcloud account](https://cloud.google.com/speech-to-text/docs/quickstart-gcloud)
3. Type the following commands into the command line.

```
$ pip install pyaudio termcolor google-cloud-speech googletrans google-cloud Pillow Gooey
$ pip install -U git+https://github.com/chriskiehl/Gooey/@issue-272-optional-radio-group-behavior
```

To transcribe audio from your audio output, you need to download [vb audio](https://vb-audio.com/Cable/index.htm) and
set your output to "CABLE Input (VB-Audio Virtual Cable)" and input to
"CABLE Output (VB-Audio Virtual Cable)".

If you just want to translate your own voice, then use your regular input device.

To begin translation/transcription, run ZoomTranslate.py.
