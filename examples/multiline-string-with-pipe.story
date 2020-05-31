Multiline strings with pipe:
  about: |
    From https://github.com/crdoconnor/strictyaml/issues/94
  given:
    string: |
      x: |
        This is a 
        multiline string
  steps:
  - lexed as: x
