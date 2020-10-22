#!/usr/bin/env python

################################################################################
# Copyright (C) 2014, 2015 GenAP, McGill University and Genome Quebec Innovation Centre
#
# This file is part of MUGQIC Pipelines.
#
# MUGQIC Pipelines is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MUGQIC Pipelines is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with MUGQIC Pipelines.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

# Python Standard Modules
import os
import zipfile
# MUGQIC Modules
from core.config import *
from core.job import *

def merge_fastq(fastq1_list, fastq2_list, out_dir, ini_section='merge_fastq'):

    other_options = config.param(ini_section, 'other_options', required=False)
    outfastq1 = os.path.join(out_dir, "merged.pair1.fastq")
    outfastq2 = os.path.join(out_dir, "merged.pair2.fastq")

    return Job(
        fastq1_list + fastq2_list,
        [outfastq1, outfastq2],
        [],
        command="""\
cat {input1} > {output1} && \\
cat {input2} > {output2}""".format(
        input1=" ".join(fastq1_list),    
        output1=outfastq1,
        input2=" ".join(fastq2_list),    
        output2=outfastq2
        )
    )
