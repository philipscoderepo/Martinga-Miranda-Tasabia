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