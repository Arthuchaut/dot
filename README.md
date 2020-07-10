# Dot

An ugly language "interpreter" inspired by Brainfuck... I'm boring. And yes, it's Python... Ugly as I said. Actually I don't know why I'm writing this README right now. Maybe I need some vacation. I was thinking about traveling to the south... I like dolphins. 

Oh, and this shit works btw. 🐬

**Note:** Any reason about the usage of Hexademical notation. Just for fun. 🐒

## Dot notation

| Command  | Definition                                                                        |
| -------- | --------------------------------------------------------------------------------- |
| SP       | Instruction separator                                                             |
| .        | Increment the "pointer"                                                           |
| ..       | Decrement the "pointer"                                                           |
| ...      | Increment the value of the memory cell                                            |
| ....     | Decrement the value of the memory cell                                            |
| .....    | Display the value of the current "pointer" value in memory set                    |
| ......   | Write the value passed (int) in the memory cell targeted by the current "pointer" |
| .......  | Jump next the corresponding ........ if the value targeted is 0x0                 |
| ........ | Jump next the corresponding ...... command if the value targeted is not 0x0       |