Mapping with hierarchy:
  about: |
    From https://github.com/crdoconnor/strictyaml/issues/94
  given:
    string: |
      a:
        c: d
        e: f
  steps:
  - lexed as: x

  
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
  - lexed as: x

    
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

  
