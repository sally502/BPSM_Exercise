
#!/bin/bash

# Input file
input="blastoutput2.out"

if [ ! -f "$input" ]; then
    echo "Error: $input not found"
    exit 1
fi

# Temporary file for sorting HSPs by bit score
tmpfile=$(mktemp)
trap 'rm -f "$tmpfile"' EXIT

# Store the number of HSPs for each subject
declare -A subject_count

# Counters
short_count=0
few_mismatch_count=0
hsp_count=0
score_high=0
score_medium=0
score_low=0
score_very_low=0

echo "===== 1. Subject accession for all HSPs ====="

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    # Skip comment lines
    [[ -z "$query" || "$query" == \#* ]] && continue

    hsp_count=$((hsp_count + 1))
    subject_count["$subject"]=$(( ${subject_count["$subject"]:-0} + 1 ))

    # Save each HSP for later sorting
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$query" "$subject" "$identity" "$aln" "$mismatches" \
        "$gapopens" "$qstart" "$qend" "$sstart" "$send" \
        "$evalue" "$bitscore" >> "$tmpfile"

    # 1. Subject accession
    echo "$subject"

done < "$input"

echo
echo "===== 2. Alignment length and percent identity ====="

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue
    printf 'Length: %s\tIdentity: %s%%\n' "$aln" "$identity"
done < "$input"

echo
echo "===== 3. HSPs with more than 20 mismatches ====="

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue
    if (( mismatches > 20 )); then
        printf '%s\t%s\t%s\t%s\n' "$subject" "$aln" "$mismatches" "$bitscore"
    fi
done < "$input"

echo
echo "===== 4. HSPs shorter than 100 aa and with >20 mismatches ====="

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue
    if (( aln < 100 && mismatches > 20 )); then
        printf '%s\tLength: %s\tMismatches: %s\n' "$subject" "$aln" "$mismatches"
    fi
done < "$input"

echo
echo "===== 5. First 20 HSPs with fewer than 20 mismatches ====="

few_mismatch_count=0

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue

    if (( mismatches < 20 )); then
        printf '%s\tLength: %s\tMismatches: %s\n' "$subject" "$aln" "$mismatches"
        few_mismatch_count=$((few_mismatch_count + 1))
        if (( few_mismatch_count == 20 )); then
            break
        fi
    fi
done < "$input"

echo
echo "===== 6. Number of HSPs shorter than 100 aa ====="

short_count=0

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue
    if (( aln < 100 )); then
        short_count=$((short_count + 1))
    fi
done < "$input"

echo "$short_count"

echo
echo "===== 7. Top 10 HSPs by bit score ====="

sort -t $'\t' -k12,12nr "$tmpfile" | head -n 10

echo
echo "===== 8. Start positions where subject accession contains AEI ====="

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue

    if [[ "$subject" == *AEI* ]]; then
        printf 'Subject: %s\tQuery start: %s\tSubject start: %s\n' \
            "$subject" "$qstart" "$sstart"
    fi
done < "$input"

echo
echo "===== 9. Number of subject sequences with more than one HSP ====="

multiple_count=0

for subject in "${!subject_count[@]}"
do
    if (( subject_count["$subject"] > 1 )); then
        multiple_count=$((multiple_count + 1))
    fi
done

echo "$multiple_count"

echo
echo "===== 10. Percentage of each HSP made up of mismatches ====="

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue

    if (( aln > 0 )); then
        percentage=$(awk -v m="$mismatches" -v l="$aln" \
            'BEGIN {printf "%.2f", 100*m/l}')
        printf '%s\tMismatch percentage: %s%%\n' "$subject" "$percentage"
    fi
done < "$input"

echo
echo "===== 11. Group HSPs by bit score ====="

score_high=0
score_medium=0
score_low=0
score_very_low=0

while IFS=$'\t' read -r query subject identity aln mismatches gapopens qstart qend sstart send evalue bitscore
do
    [[ -z "$query" || "$query" == \#* ]] && continue

    if (( bitscore >= 300 )); then
        score_high=$((score_high + 1))
    elif (( bitscore >= 200 )); then
        score_medium=$((score_medium + 1))
    elif (( bitscore >= 100 )); then
        score_low=$((score_low + 1))
    else
        score_very_low=$((score_very_low + 1))
    fi
done < "$input"

echo "Bit score >= 300: $score_high"
echo "Bit score 200-299: $score_medium"
echo "Bit score 100-199: $score_low"
echo "Bit score < 100: $score_very_low"
