HELP_TEXT = """
Available Commands:
  help                      - Show this help message
  list                      - Show all created shapes
  exit                      - Close the application

  create <SHAPE> <ARGS>     - Create a new shape
  delete <ID>               - Remove a shape by its ID

  length <ID>               - Calculate the length of a shape
  area <ID>                 - Calculate the area of a shape
  perimeter <ID>            - Calculate the perimeter of a shape
  
  distance <ID1> <ID2>      - Calculate distance between two shapes
  translate <ID> <DX> <DY>  - Move a shape by DX and DY coordinates
  compare <ID1> <ID2>       - Compare two shapes by their area

Shape Creation Guide:
  create point <X> <Y>
  create segment <X1> <Y1> <X2> <Y2>
  create circle <X> <Y> <RADIUS>
  create square <X> <Y> <SIDE>
""".strip()
