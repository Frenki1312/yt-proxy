from flask import Flask, redirect, request
import yt_dlp

app = Flask(__name__)


@app.route('/stream')
def stream():
  yt_url = request.args.get('url')
  if not yt_url:
    return 'Nedostaje URL', 400

  ydl_opts = {'format': 'best[ext=mp4]/best'}
  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(yt_url, download=False)
      return redirect(info['url'])
  except Exception as e:
    return str(e), 500


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)