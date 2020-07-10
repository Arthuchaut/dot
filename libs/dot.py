from typing import Dict, Callable
import sys

class Dot:
    def __init__(self):
        self._mem_set: List[hex] = []
        self._ptr: int = -1
        self._cmds: List[str] = None
        self._cmd_index: int = 0
        self._cmd_map: Dict[str, Callable] = {
            '.'    : self._incr_ptr,
            '.' * 2: self._decr_ptr,
            '.' * 3: self._incr_hex,
            '.' * 4: self._decr_hex,
            '.' * 5: self._ascii_output,
            '.' * 6: self._ascii_input,
            '.' * 7: self._jump_forward,
            '.' * 8: self._jump_behind,
        }

    def run(self, dot_code: str) -> None:
        self._cmds: List[str] = dot_code.split(' ')

        while self._cmd_index < len(self._cmds):
            try:
                self._cmd_map[self._cmds[self._cmd_index]]()
                self._cmd_index += 1
            except KeyError:
                raise DotRunnerError(
                    f'Unknown command: {self._cmds[self._cmd_index]} '
                    f'at index {self._cmd_index}. '
                    f'Dot runner exited.'
                )

    def _incr_ptr(self) -> None:
        self._ptr += 1

        if self._ptr > len(self._mem_set) - 1:
            self._mem_set += [0x0]

    def _decr_ptr(self) -> None:
        self._ptr -= 1

        if self._ptr < 0:
            raise DotRunnerError('Pointer out of memory bound.')

    def _incr_hex(self) -> None:
        self._mem_set[self._ptr] += 0x1

    def _decr_hex(self) -> None:
        self._mem_set[self._ptr] -= 0x1

    def _ascii_output(self) -> None:
        sys.stdout.write(chr(self._mem_set[self._ptr]))

    def _ascii_input(self) -> None:
        try:
            h: hex = hex(int(sys.stdin.read(1)))
        except ValueError:
            raise DotRunnerError('Stdin value must be an integer.')

        self._mem_set[self._ptr] = h

    def _jump_forward(self) -> None:
        # Decrement by 1 (because automaticly incremented in the while loop).
        # Need to think...
        ...

    def _jump_behind(self) -> None:
        # Decrement by 1 (because automaticly incremented in the while loop).
        # Need to think...
        ...

class DotRunnerError(Exception):
    pass