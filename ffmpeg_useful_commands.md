###Remove metadata:
`ffmpeg -i in.mov -map_metadata -1 -c:v copy -c:a copy out.mov`