#!/bin/bash

set -euo pipefail

#define inputs taxid and gene
TAXID="${1:?Usage: bash plotcon_pipeline.sh TAXID GENE}"
GENE="${2:?Usage: bash plotcon_pipeline.sh TAXID GENE}"

#output directory
OUTDIR="${TAXID}_${GENE}"
mkdir -p "$OUTDIR"

RAW="$OUTDIR/sequences.fasta"
ALIGNED="$OUTDIR/aligned.fasta"

#1.retrieve sequences
QUERY="txid${TAXID}[Organism:exp] AND ${GENE}[Gene Name] NOT partial[Title]"

esearch -db protein -query "$QUERY" | efetch -format fasta > "$RAW"

#2. check input
NSEQ=$(grep -c '^>' "$RAW" || true)

if [ "$NSEQ" -lt 30 ] || [ "$NSEQ" -gt 600 ]; then
	echo "Unexpected sequence count: $NSEQ" >&2
	exit 1
fi

#3. align sequences
clustalo -i "$RAW" -o "$ALIGNED" --outfmt=fasta --force

#4.use plotcon to generate conservation maps
for WIN in 4 10 20
do
	plotcon -sequences "$ALIGNED" -winsize "$WIN" -graph png \
	-goutfile "$OUTDIR/conservation_w${WIN}.png" -auto
done

echo "Pipeline completed :$OUTDIR"

