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
  - lexed as: x
