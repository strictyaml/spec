Comments:
  about: |
    From https://github.com/crdoconnor/strictyaml/issues/94
  given:
    string: |
      # This is a comment

      key: a value # an inline comment
      another key: value

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
              "pos": 21,
              "text": "\n\n",
              "type": "NL_INDENT"
          },
          {
              "pos": 24,
              "text": "key",
              "type": "TEXT"
          },
          {
              "pos": 26,
              "text": ": ",
              "type": "COLON_SPACE"
          },
          {
              "pos": 53,
              "text": "a value # an inline comment",
              "type": "TEXT"
          },
          {
              "pos": 54,
              "text": "\n",
              "type": "NL"
          },
          {
              "pos": 65,
              "text": "another key",
              "type": "TEXT"
          },
          {
              "pos": 67,
              "text": ": ",
              "type": "COLON_SPACE"
          },
          {
              "pos": 72,
              "text": "value",
              "type": "TEXT"
          },
          {
              "pos": 74,
              "text": "\n\n",
              "type": "NL_INDENT"
          },
          {
              "pos": 103,
              "text": "# This is yet another comment",
              "type": "TEXT"
          },
          {
              "pos": 104,
              "text": "\n",
              "type": "NL"
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
