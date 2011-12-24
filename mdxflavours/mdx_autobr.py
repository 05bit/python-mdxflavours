# -*- coding: utf-8 -*-

"""
ABOUT

Auto line break preprocessor for Markdown. Transforms line
breaks to <br/>.

You should place this snippet as file 'mdx_autobr.py' to
some dir in PYTHON_PATH, as described in docs here:
http://www.freewisdom.org/projects/python-markdown/Using_as_a_Module

LICENSE

Copyright 2009 Alexey Kinyov <rudi@05bit.com>. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY ALEXEY KINYOV ``AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ALEXEY KINYOV OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of Alexey Kinyov.

"""

import markdown

class AutoBrPreprocessor(markdown.preprocessors.Preprocessor):
    def run(self, lines):
        br_sp = '  '
        line, new_lines = (None, [])
        for next in lines:
            if not line is None:
                if (next and line and line[-2:] != br_sp): line += br_sp
                new_lines.append(line)
            line = next
        if not line is None: new_lines.append(line)
        return new_lines

class AutoBrExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('autobr', AutoBrPreprocessor(md), "_begin")

def makeExtension(configs=None):
    return AutoBrExtension(configs=configs)