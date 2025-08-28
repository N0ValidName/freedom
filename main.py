from attribute.html import initialize_html_attributes
from attribute.svg import initialize_svg_attributes
from js.function.svg import initialize_svg_functions
from js.property.svg import initialize_svg_properties
from js.function.html import initialize_html_functions
from js.property.html import initialize_html_properties
from js.misc import initialize_misc_apis

from fuzzer import Fuzzer
from db import Manager

import os
import sys
import time
import math
import random
import argparse
from enum import Enum

sys.setrecursionlimit(3000)


def init():
    usec, sec = math.modf(time.time())
    random.seed(int.from_bytes(os.urandom(4), byteorder='little') ^ int(usec * 1e6) ^ os.getpid())
    initialize_html_attributes()
    initialize_html_functions()
    initialize_html_properties()
    initialize_svg_attributes()
    initialize_svg_functions()
    initialize_svg_properties()
    initialize_misc_apis()


class FuzzMode(Enum):
    GenerateOnly = 0  # Test
    ArkTSGenerate = 1  # ArkTS Generation
    HybridGenerate = 2  # Both DOM and ArkTS


fuzz_modes = {
    "generate": FuzzMode.GenerateOnly,
    "arkts-generate": FuzzMode.ArkTSGenerate,
    "hybrid": FuzzMode.HybridGenerate,
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A DOM and ArkTS fuzzer for OpenHarmony applications')
    parser.add_argument("-m", dest="mode", help="Fuzzing mode: generate (DOM only), arkts-generate (ArkTS only), or hybrid (both)")
    parser.add_argument("-n", dest="num", help="Number of generated testcases", required=False)
    parser.add_argument("-i", dest="index", help="Fuzzer ID")
    parser.add_argument("-o", dest="output", required=False, help="Output directory for generated files")
    args = parser.parse_args()

    mode = fuzz_modes.get(args.mode)
    if mode is None:
        parser.print_help()
        sys.exit(1)

    init()

    if mode == FuzzMode.GenerateOnly:
        if args.output is None or args.num is None:
            print("Number of testcases (-n) and output directory (-o) are required in generated-only mode.")
            sys.exit(1)

        manager = Manager(int(args.index), True, args.output)
        fuzzer = Fuzzer(None, manager)
        fuzzer.generate_only(int(args.num))
    elif mode == FuzzMode.ArkTSGenerate:
        if args.output is None or args.num is None:
            print("Number of testcases (-n) and output directory (-o) are required in ArkTS generation mode.")
            sys.exit(1)

        manager = Manager(int(args.index), True, args.output, file_extension=".ets")
        fuzzer = Fuzzer(None, manager)
        fuzzer.generate_arkts_only(int(args.num))
    elif mode == FuzzMode.HybridGenerate:
        if args.output is None or args.num is None:
            print("Number of testcases (-n) and output directory (-o) are required in hybrid generation mode.")
            sys.exit(1)

        manager = Manager(int(args.index), True, args.output)
        fuzzer = Fuzzer(None, manager)
        fuzzer.generate_hybrid(int(args.num))
    else:
        pass
