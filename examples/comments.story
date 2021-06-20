Comments:
  about: |
    From https://github.com/crdoconnor/strictyaml/issues/94
  given:
    string: |
      # This is a comment

      a: x # another comment
      b: c

      # This is yet another comment
  steps:
  - lexed as: |-
      [
          {
              "pos": 19,
              "text": "# This is a comment",
              "type": "TEXT"
          },
          {
              "pos": 20,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 21,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 22,
              "text": "a",
              "type": "TEXT"
          },
          {
              "pos": 24,
              "text": ": ",
              "type": "COLONSPACE"
          },
          {
              "pos": 43,
              "text": "x # another comment",
              "type": "TEXT"
          },
          {
              "pos": 44,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 45,
              "text": "b",
              "type": "TEXT"
          },
          {
              "pos": 47,
              "text": ": ",
              "type": "COLONSPACE"
          },
          {
              "pos": 48,
              "text": "c",
              "type": "TEXT"
          },
          {
              "pos": 49,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 50,
              "text": "\n",
              "type": "NEWLINE"
          },
          {
              "pos": 79,
              "text": "# This is yet another comment",
              "type": "TEXT"
          },
          {
              "pos": 80,
              "text": "\n",
              "type": "NEWLINE"
          }
      ]
  - parsed as: |-
      [
          {
              "text": "# This is a comment",
              "type": "COMMENT"
          },
          {
              "text": "# This is yet another comment",
              "type": "COMMENT"
          }
      ]
