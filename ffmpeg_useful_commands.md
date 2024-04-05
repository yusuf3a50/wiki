### Remove metadata:
`ffmpeg -i in.mov -map_metadata -1 -c:v copy -c:a copy out.mov`

### Remove rotate metadata
check rotate metadata first:
`ffmpeg -i input.m4v 2>&1  | grep rotate`
### Remove `rotate` metadata:
`ffmpeg -i input.mp4 -c copy -metadata:s:v:0 rotate="0" output.mp4`

##### Rotate video:
`ffmpeg -i input.mp4 -vf "transpose=1" output.mp4`
##### Preview before changing
`ffplay -vf "transpose=1" -i input.mp4`

    0 = 90° counter-clockwise and vertical flip (default)
    1 = 90° clockwise
    2 = 90° counter-clockwise
    3 = 90° clockwise and vertical flip

[More documentation](https://www.baeldung.com/linux/ffmpeg-rotate-video)

#### Cut/trim

##### Cut using a specific time

`ffmpeg -i input.mp4 -ss 00:05:10 -to 00:15:30 -c:v copy -c:a copy output2.mp4`

The above command uses -to to specify an exact time to cut to from the starting position. The cut video will be from 00:05:10 to 00:15:30, resulting in a 10 minutes and 20 seconds video.

[More documentation](https://shotstack.io/learn/use-ffmpeg-to-trim-video/)

### Remove audio
You remove audio by using the -an flag:

`ffmpeg -i input_file.mkv -c copy -an output_file-noSound.mkv`