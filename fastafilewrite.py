                              
from Bio import SeqIO                     # import to parse files
import re

states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
new_states = ['|' + new_str for new_str in states]


north_states = ['|ME', '|NY', '|NJ', '|VT', '|MA', '|RI', '|CT', '|NH', '|PA']


# Function to write information about Texas to a file
def open_glyco():

    with open("/Users/islam/Desktop/Books/AllSurfaceGlycoproteinSeqs.fasta") as glyco:        # Opening the file
        all_out = open("/Users/islam/Desktop/Books/TX_MSA.fasta", 'w') # Opening the file to where the info would be written
        north_out = open("/Users/islam/Desktop/Books/Northeast.fasta", 'w')
        
        for record in SeqIO.parse(glyco, 'fasta'): # for loop and SeqIO to parse through fasta file
            state_id = record.id
            state_desc = record.description 
            state_seq = record.seq[319:514]                       # getting specific info
            
                                      # for loop to find TX and outputting it
         
            #if any(item in str(new_states) for item in TX_desc) is True:           # if statement to find only Texas info,if '|TX'
            if '|TX' in state_id:   
             #   #out.write('>{}:'.format(TX_id))                   # Writing info to new file
                all_out.write('>{}:\n'.format(state_desc))
                all_out.write('{}:\n'.format(state_seq))
            


    
def north_east():
    
    #north_out = open("/Users/islam/Desktop/Books/Northeast.fasta", 'w')
    north_out = open("/Users/islam/Desktop/Books/Northeast.fasta", 'w')
    if all(item in str(north_states) for item in state_desc):
           # if str(north_states) in state_desc:
            #if a in state_desc:
                north_out.write('>{}:\n'.format(state_desc))
                north_out.write('{}:\n'.format(state_seq))

                
    north_out.close()                         # Closing the file
def all_execute():
    open_glyco()
    north_east()