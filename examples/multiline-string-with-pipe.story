Multiline strings with pipe:
  about: |
    From https://github.com/crdoconnor/strictyaml/issues/94
  given:
    string: |
      x: |
        This is a 
        multiline string
  steps:
  - lexed as: |-
      [
          {
              "pos": 1,
              "text": "x",
              "type": "TEXT"
          },
          {
              "pos": 3,
              "text": ": ",
              "type": "COLONSPACE"
          },
          {
              "pos": 4,
              "text": "|",
              "type": "TEXT"
          },
          {
              "pos": 5,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 17,
              "text": "  This is a ",
              "type": "TEXT"
          },
          {
              "pos": 18,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 36,
              "text": "  multiline string",
              "type": "TEXT"
          },
          {
              "pos": 37,
              "text": "\n",
              "type": "NEWLINE"
          }
      ]
