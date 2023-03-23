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