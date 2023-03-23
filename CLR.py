def convert_vcf_tsv():
    input_vcf = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA.vcf" #hardcoded value, always put on top
    output_bed = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA.tsv"
    output_write = open(output_bed,mode='w')

    with open(input_vcf, mode='r') as vcf_data:
        for sv in vcf_data:
            if "#" in sv[0]:
                continue
            sv_list = sv.split("\t")
            chr = sv_list[0]
            pos = sv_list[1]
            info = sv_list[7].split(";")
            bed_list = list()
            bed_list.append(chr)
            bed_list.append(pos)
            for info_entry in info:
                temp = info_entry.split("=")
                bed_list.append(temp[1])

            output_write.write("\t".join(str(x) for x in bed_list)+"\n") #join is the opposite of split, convert list into sentence

# Write Bed Files
def write_bed_files():
    orig_bed = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA.tsv"
    snv_bed = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA_snv.tsv"
    snv_write = open(snv_bed, mode='w')
    indel_lt_bed = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA_indel_lt50bp.tsv"
    indel_lt_write = open(indel_lt_bed,mode='w')
    ins_gt_bed = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA_ins_gt50bp.tsv"
    ins_gt_write = open(ins_gt_bed,mode='w')
    del_gt_bed = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA_del_gt50bp.tsv"
    del_gt_write = open(del_gt_bed,mode='w')
    inv_bed = "/Users/miranm/Desktop/rotation_data/CLR/pav_DBA_inv.tsv"
    inv_write = open(inv_bed,mode='w')

    with open(orig_bed, mode='r') as data:
        for variant in data:
            l = variant.split("\n")[0].split("\t")
            chr = l[0]
            start = l[1]
            id = l[2]
            end = id.split("-")[1]
            var = l[3]
            bed_list = list()
            bed_list.append(chr)
            bed_list.append(start)
            if var == 'DEL' or var == 'INV':
                bed_list.append(end)
            bed_list.append(id)
            bed_list.append(var)
            if var == 'SNV':
                bed_list.append(l[5])
                snv_write.write("\t".join(str(x) for x in bed_list) + "\n")
            if (var == 'INS' or var == 'DEL'):
                indel_length = int(id.split("-")[3])
                if (abs(indel_length) < 50):
                    qs = l[6]
                    ref = l[7]
                    tig = l[8]
                    bed_list.append(qs)
                    bed_list.append(ref)
                    bed_list.append(tig)
                    indel_lt_write.write("\t".join(str(x) for x in bed_list)+"\n")
            if var == 'INS':
                indel_length = int(id.split("-")[3])
                if (abs(indel_length) >= 50):
                    qs = l[6]
                    ref = l[7]
                    tig = l[8]
                    bed_list.append(qs)
                    bed_list.append(ref)
                    bed_list.append(tig)
                    ins_gt_write.write("\t".join(str(x) for x in bed_list) + "\n")
            if var == 'DEL':
                indel_length = int(id.split("-")[3])
                if (abs(indel_length) >= 50):
                    qs = l[6]
                    ref = l[7]
                    tig = l[8]
                    bed_list.append(qs)
                    bed_list.append(ref)
                    bed_list.append(tig)
                    del_gt_write.write("\t".join(str(x) for x in bed_list) + "\n")
            if var == 'INV':
                qs = l[6]
                ref = l[7]
                tig = l[8]
                bed_list.append(qs)
                bed_list.append(ref)
                bed_list.append(tig)
                inv_write.write("\t".join(str(x) for x in bed_list) + "\n")

import os
import csv
from xlsxwriter.workbook import Workbook

def convert_tsv_xlsx(directory):
    os.chdir(directory)

    for beds in os.listdir(directory):
        tsv_reader = csv.reader(open(beds, 'rt'), delimiter='\t')
        if beds.endswith(".tsv"):
            new_filename = beds.replace(".tsv",".xlsx")
            workbook = Workbook(new_filename)
            worksheet = workbook.add_worksheet()
            for row, data in enumerate(tsv_reader):
                worksheet.write_row(row, 0, data)
            workbook.close()

convert_vcf_tsv()
write_bed_files()
convert_tsv_xlsx("/Users/miranm/Desktop/rotation_data/CLR")