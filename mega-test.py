a = {
  "id": "chatcmpl-8rPQP1HxHdOk6rgOMLIq4YndZZoUh",
  "object": "chat.completion",
  "created": 1707739809,
  "model": "gpt-4-32k",
  "prompt_filter_results": [
    {
      "prompt_index": 0,
      "content_filter_results": {
        "hate": {
          "filtered": False,
          "severity": "safe"
        },
        "self_harm": {
          "filtered": False,
          "severity": "safe"
        },
        "sexual": {
          "filtered": False,
          "severity": "safe"
        },
        "violence": {
          "filtered": False,
          "severity": "safe"
        }
      }
    }
  ],
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "[{'timestamp': [0.0, 9.0], 'text': \" He's nailed this. He's high in the air. He's got enough. Oh, yes, he does. He's six.\"},\n{'timestamp': [20.0, 25.0], 'text': \" picked it up the six pressure on Anderson. Ornith looks at it. That's good for a young gun.\"},\n{'timestamp': [33.0, 34.0], 'text': \" And he's got not got this.\"},\n{'timestamp': [36.0, 38.0], 'text': ' Right, 19.1.'},\n{'timestamp': [39.0, 41.0], 'text': ' The 194 for three New Zealand.'},\n{'timestamp': [41.0, 43.0], 'text': ' 192 for five England.'},\n{'timestamp': [63.0, 65.0], 'text': \" that's better. Dot ball. That ball for New Zealand went\"},\n{'timestamp': [65.0, 66.0], 'text': ' for four.'},\n{'timestamp': [103.0, 105.0], 'text': \" Tries the bounce and he's pulled into the leg side. He's got the crowd. Robbie Bupara has got the crowd. Fancy a nine. He's got the crowd.\"},\n{'timestamp': [133.46, 135.62], 'text': ' Down to a T20 here.'},\n{'timestamp': [185.0, 187.0], 'text': ' Like a side salad Cori Anderson. Good recovery is this.'},\n{'timestamp': [187.0, 189.0], 'text': ' Six off the first ball.'},\n{'timestamp': [205.88, 207.72], 'text': ' The final eight off two.'},\n{'timestamp': [208.44, 211.32], 'text': ' Left hand, though, hitting to the short boundary now.'},\n{'timestamp': [247.0, 250.0], 'text': ' Six for a super over.'},\n{'timestamp': [250.0, 252.0], 'text': ' And came super over.'},\n{'timestamp': [258.0, 260.0], 'text': ' Give it everything there Ben Stolkes'},\n{'timestamp': [322.52, 324.28], 'text': ' Robby with par a just a single'},\n{'timestamp': [324.28, 329.0], 'text': ' its New Zealand in a wonderfully entertaining game at T20 cricket.'},\n{'timestamp': [334.0, 336.0], 'text': ' Anderson, as did Butler.'},\n{'timestamp': [343.0, 345.36], 'text': ' Continuous changes of plans from Brendan McCullough,'}]"
      },
      "content_filter_results": {
        "hate": {
          "filtered": False,
          "severity": "safe"
        },
        "self_harm": {
          "filtered": False,
          "severity": "safe"
        },
        "sexual": {
          "filtered": False,
          "severity": "safe"
        },
        "violence": {
          "filtered": False,
          "severity": "safe"
        }
      }
    }
  ],
  "usage": {
    "prompt_tokens": 4067,
    "completion_tokens": 609,
    "total_tokens": 4676
  }
}
print(a["choices"][0]["message"]["content"])