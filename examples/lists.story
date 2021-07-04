Lists:
  about: |
    From https://github.com/crdoconnor/strictyaml/issues/94
  given:
    string: |
      a:
        - 1
        - 2
        - 3
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
              "pos": 5,
              "text": "\n  ",
              "type": "NL_INDENT"
          },
          {
              "pos": 8,
              "text": "- 1",
              "type": "TEXT"
          },
          {
              "pos": 11,
              "text": "\n  ",
              "type": "NL_INDENT"
          },
          {
              "pos": 14,
              "text": "- 2",
              "type": "TEXT"
          },
          {
              "pos": 17,
              "text": "\n  ",
              "type": "NL_INDENT"
          },
          {
              "pos": 20,
              "text": "- 3",
              "type": "TEXT"
          },
          {
              "pos": 21,
              "text": "\n",
              "type": "NL"
          }
      ]
  - parsed as: |-
      [
          {
              "text": "1",
              "type": "LI"
          },
          {
              "text": "2",
              "type": "LI"
          },
          {
              "text": "3",
              "type": "LI"
          }
      ]
