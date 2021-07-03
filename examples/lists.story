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
              "pos": 3,
              "text": ":\n",
              "type": "COLONSPACE"
          },
          {
              "pos": 6,
              "text": "- 1",
              "type": "TEXT"
          },
          {
              "pos": 7,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 10,
              "text": "- 2",
              "type": "TEXT"
          },
          {
              "pos": 11,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 14,
              "text": "- 3",
              "type": "TEXT"
          },
          {
              "pos": 15,
              "text": "\n",
              "type": "NEWLINE"
          }
      ]
  - parsed as: |-
      [
          {
              "text": "a",
              "type": "KEY"
          },
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
