#!/bin/bash

#[1]QC1:perform a quality check on the gzip compressed fastq format paired-end raw sequence data
# using the installed fastqc programme

#define input directory and create a new output directory
unset IFS
INDIR="${1}"
OUTDIR="${INDIR}_results"
mkdir -p "${OUTDIR}"

fastqc -o "${OUTDIR}" "${INDIR}"/*.fq.gz

echo "fastqc check completed :$OUTDIR"

#[2]QC2:assess the numbers and quality of the raw sequence data based on the outputs of fastqc
#unzip zip file, get summary txt
SUMDIR="${INDIR}_summary"
mkdir -p "${SUMDIR}"
for zipfile in "${OUTDIR}"/*_fastqc.zip; do
	unzip "$zipfile" -d "${SUMDIR}"
done
echo "file unzipped"

#[3]Align reads to genome

