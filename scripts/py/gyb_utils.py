# GYB: Generate Your Boilerplate (improved names welcome; at least
# this one's short).  See -h output for instructions

#  Copyright (c) 2024 ScribbleLabApp LLC.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse

def autogenerated_warning(filename: str) -> str:
  """
  This function generates a warning message for auto-generated files.
  The message is formatted as a multi-line string with comments for better readability.

  Parameters:
    filename (str): The name of the file for which the warning is being generated.

  Returns:
    str: A formatted string containing the warning message.
  """

  return f"""
//
// #############################################################################
// #                                                                           #
// #            DO NOT EDIT THIS FILE; IT IS AUTOGENERATED.                    #
// #                                                                           #
// #############################################################################
//
// WARNING: This file is auto-generated by the code generation tool.
// Modifications to this file may be overwritten and lost if the code is regenerated.
// If you need to make changes, update the source schema or generation process instead.
// DO NOT EDIT THIS FILE MANUALLY.
//
// Auto-generated file: {filename}.swift
// Generated by GYB
"""

def parse_args():
    """
    Parse command line arguments.

    Returns:
      argparse.Namespace: Parsed command line arguments.
    """

    parser = argparse.ArgumentParser(description='Generate boilerplate code.')
    parser.add_argument('--template', required=True, help='Path to the template file.')
    parser.add_argument('--output', required=True, help='Path to the output file.')
    parser.add_argument('--replacements', required=True, help='JSON string of replacements.')
    return parser.parse_args()

ptr_bit_width_64 = "(compiler(>=5.9) && _pointerBitWidth(_64)) || (compiler(<5.9) && (arch(x86_64) || arch(arm64)))"