Simple mapping:
  given:
    string: |
      a: b
  steps:
  - lexed as: |-
      [
          {
              "pos": 1,
              "text": "a",
              "type": "TEXT"
          },
          {
              "pos": 2,
              "text": ":",
              "type": "COLON"
          },
          {
              "pos": 4,
              "text": " b",
              "type": "TEXT"
          },
          {
              "pos": 5,
              "text": "\n",
              "type": "NEWLINE"
          }
      ]
