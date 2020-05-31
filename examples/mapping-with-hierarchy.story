Mapping with hierarchy:
  about: |
    From https://github.com/crdoconnor/strictyaml/issues/94
  given:
    string: |
      ford:
        surname: prefect
        from: betelgeuse
  steps:
  - lexed as: |-
      [
          {
              "pos": 4,
              "text": "ford",
              "type": "TEXT"
          },
          {
              "pos": 6,
              "text": ":\n",
              "type": "COLONSPACE"
          },
          {
              "pos": 15,
              "text": "  surname",
              "type": "TEXT"
          },
          {
              "pos": 17,
              "text": ": ",
              "type": "COLONSPACE"
          },
          {
              "pos": 24,
              "text": "prefect",
              "type": "TEXT"
          },
          {
              "pos": 27,
              "text": "\n  ",
              "type": "INDENT"
          },
          {
              "pos": 31,
              "text": "from",
              "type": "TEXT"
          },
          {
              "pos": 33,
              "text": ": ",
              "type": "COLONSPACE"
          },
          {
              "pos": 43,
              "text": "betelgeuse",
              "type": "TEXT"
          },
          {
              "pos": 44,
              "text": "\n",
              "type": "NEWLINE"
          }
      ]
