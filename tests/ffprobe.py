#!/usr/bin/env python3
import unittest

from pyfastocloud.structs.ffprobe_result import FFprobeResult


class FFprobeTest(unittest.TestCase):
    def test_ffprobe(self):
        json = {
            "streams": [
                {
                    "index": 0,
                    "codec_name": "timed_id3",
                    "codec_long_name": "timed ID3 metadata",
                    "codec_type": "data",
                    "codec_tag_string": "ID3 ",
                    "codec_tag": "0x20334449",
                    "r_frame_rate": "0/0",
                    "avg_frame_rate": "0/0",
                    "time_base": "1/90000",
                    "disposition": {
                        "default": 0,
                        "dub": 0,
                        "original": 0,
                        "comment": 0,
                        "lyrics": 0,
                        "karaoke": 0,
                        "forced": 0,
                        "hearing_impaired": 0,
                        "visual_impaired": 0,
                        "clean_effects": 0,
                        "attached_pic": 0,
                        "timed_thumbnails": 0
                    },
                    "tags": {
                        "variant_bitrate": "0"
                    }
                },
                {
                    "index": 1,
                    "codec_name": "h264",
                    "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
                    "profile": "High",
                    "codec_type": "video",
                    "codec_time_base": "1/50",
                    "codec_tag_string": "[27][0][0][0]",
                    "codec_tag": "0x001b",
                    "width": 720,
                    "height": 576,
                    "coded_width": 720,
                    "coded_height": 576,
                    "closed_captions": 0,
                    "has_b_frames": 2,
                    "sample_aspect_ratio": "16:15",
                    "display_aspect_ratio": "4:3",
                    "pix_fmt": "yuv420p",
                    "level": 40,
                    "chroma_location": "left",
                    "refs": 1,
                    "is_avc": "false",
                    "nal_length_size": "0",
                    "r_frame_rate": "25/1",
                    "avg_frame_rate": "25/1",
                    "time_base": "1/90000",
                    "start_pts": 4881610620,
                    "start_time": "54240.118000",
                    "bits_per_raw_sample": "8",
                    "disposition": {
                        "default": 0,
                        "dub": 0,
                        "original": 0,
                        "comment": 0,
                        "lyrics": 0,
                        "karaoke": 0,
                        "forced": 0,
                        "hearing_impaired": 0,
                        "visual_impaired": 0,
                        "clean_effects": 0,
                        "attached_pic": 0,
                        "timed_thumbnails": 0
                    },
                    "tags": {
                        "variant_bitrate": "0"
                    }
                },
                {
                    "index": 2,
                    "codec_name": "aac",
                    "codec_long_name": "AAC (Advanced Audio Coding)",
                    "profile": "LC",
                    "codec_type": "audio",
                    "codec_time_base": "1/48000",
                    "codec_tag_string": "[15][0][0][0]",
                    "codec_tag": "0x000f",
                    "sample_fmt": "fltp",
                    "sample_rate": "48000",
                    "channels": 2,
                    "channel_layout": "stereo",
                    "bits_per_sample": 0,
                    "r_frame_rate": "0/0",
                    "avg_frame_rate": "0/0",
                    "time_base": "1/90000",
                    "start_pts": 4881609750,
                    "start_time": "54240.108333",
                    "disposition": {
                        "default": 0,
                        "dub": 0,
                        "original": 0,
                        "comment": 0,
                        "lyrics": 0,
                        "karaoke": 0,
                        "forced": 0,
                        "hearing_impaired": 0,
                        "visual_impaired": 0,
                        "clean_effects": 0,
                        "attached_pic": 0,
                        "timed_thumbnails": 0
                    },
                    "tags": {
                        "variant_bitrate": "0"
                    }
                }
            ],
            "format": {
                "filename": "https://some/chunklist.m3u8",
                "nb_streams": 3,
                "nb_programs": 1,
                "format_name": "hls",
                "format_long_name": "Apple HTTP Live Streaming",
                "start_time": "54240.108333",
                "size": "194",
                "probe_score": 100
            }
        }

        ffprobe = FFprobeResult.make_entry(json)
        self.assertEqual(len(ffprobe.streams), 3)
        self.assertEqual(ffprobe.format['nb_streams'], 3)
        self.assertTrue(ffprobe.is_live())

        json2 = {
            "streams": [
                {
                    "index": 0,
                    "codec_name": "h264",
                    "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
                    "profile": "Main",
                    "codec_type": "video",
                    "codec_time_base": "1/60",
                    "codec_tag_string": "avc1",
                    "codec_tag": "0x31637661",
                    "width": 1280,
                    "height": 720,
                    "coded_width": 1280,
                    "coded_height": 720,
                    "closed_captions": 0,
                    "has_b_frames": 1,
                    "sample_aspect_ratio": "1:1",
                    "display_aspect_ratio": "16:9",
                    "pix_fmt": "yuv420p",
                    "level": 31,
                    "color_range": "tv",
                    "color_space": "bt709",
                    "color_transfer": "bt709",
                    "color_primaries": "bt709",
                    "chroma_location": "left",
                    "refs": 1,
                    "is_avc": "true",
                    "nal_length_size": "4",
                    "r_frame_rate": "30/1",
                    "avg_frame_rate": "30/1",
                    "time_base": "1/15360",
                    "start_pts": 0,
                    "start_time": "0.000000",
                    "duration_ts": 1137152,
                    "duration": "74.033333",
                    "bit_rate": "4451073",
                    "bits_per_raw_sample": "8",
                    "nb_frames": "2221",
                    "disposition": {
                        "default": 1,
                        "dub": 0,
                        "original": 0,
                        "comment": 0,
                        "lyrics": 0,
                        "karaoke": 0,
                        "forced": 0,
                        "hearing_impaired": 0,
                        "visual_impaired": 0,
                        "clean_effects": 0,
                        "attached_pic": 0,
                        "timed_thumbnails": 0
                    },
                    "tags": {
                        "creation_time": "2021-01-13T10:47:28.000000Z",
                        "language": "und",
                        "handler_name": "ISO Media file produced by Google Inc. Created on: 01/13/2021."
                    }
                },
                {
                    "index": 1,
                    "codec_name": "aac",
                    "codec_long_name": "AAC (Advanced Audio Coding)",
                    "profile": "LC",
                    "codec_type": "audio",
                    "codec_time_base": "1/44100",
                    "codec_tag_string": "mp4a",
                    "codec_tag": "0x6134706d",
                    "sample_fmt": "fltp",
                    "sample_rate": "44100",
                    "channels": 2,
                    "channel_layout": "stereo",
                    "bits_per_sample": 0,
                    "r_frame_rate": "0/0",
                    "avg_frame_rate": "0/0",
                    "time_base": "1/44100",
                    "start_pts": 0,
                    "start_time": "0.000000",
                    "duration_ts": 3265536,
                    "duration": "74.048435",
                    "bit_rate": "128037",
                    "nb_frames": "3189",
                    "disposition": {
                        "default": 1,
                        "dub": 0,
                        "original": 0,
                        "comment": 0,
                        "lyrics": 0,
                        "karaoke": 0,
                        "forced": 0,
                        "hearing_impaired": 0,
                        "visual_impaired": 0,
                        "clean_effects": 0,
                        "attached_pic": 0,
                        "timed_thumbnails": 0
                    },
                    "tags": {
                        "creation_time": "2021-01-13T10:47:28.000000Z",
                        "language": "und",
                        "handler_name": "ISO Media file produced by Google Inc. Created on: 01/13/2021."
                    }
                }
            ],
            "format": {
                "filename": "",
                "nb_streams": 2,
                "nb_programs": 0,
                "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
                "format_long_name": "QuickTime / MOV",
                "start_time": "0.000000",
                "duration": "74.048372",
                "size": "42414042",
                "bit_rate": "4582306",
                "probe_score": 100,
                "tags": {
                    "major_brand": "mp42",
                    "minor_version": "0",
                    "compatible_brands": "isommp42",
                    "creation_time": "2021-01-13T10:47:28.000000Z"
                }
            }
        }

        ffprobe2 = FFprobeResult.make_entry(json2)
        self.assertEqual(len(ffprobe2.streams), 2)
        self.assertEqual(ffprobe2.format['nb_streams'], 2)
        self.assertFalse(ffprobe2.is_live())
        self.assertEqual(ffprobe2.duration, 74048)


if __name__ == '__main__':
    unittest.main()
