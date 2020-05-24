# Initialize program arguments, see help= for explanation of each
parser = argparse.ArgumentParser()
parser.add_argument("--query",type=str,help='Path to kmer count file for sequences of interest (e.g. functional regions of a ncRNA)')
parser.add_argument('--null', type=str,help='Path to kmer count file that compose null model (e.g. transcriptome, genome, etc.)')
parser.add_argument('--qT',type=float,help='Probability of query to query transition',default=.999)
parser.add_argument('--nT',type=float,help='Probability of null to null transition',default=.9999)
parser.add_argument('--qPrefix',type=str,help='String, Output file prefix;default=None',default='query')
parser.add_argument('--nPrefix',type=str,help='String, Output file prefix;default=None',default='null')
parser.add_argument('--dir',type=str,help='Output directory',default='./')
parser.add_argument('-k',type=str,help='Comma delimited string of possible k-mer values,must be found in the k-mer count file',default='2,3,4')
parser.add_argument('-a',type=str,help='String, Alphabet to generate k-mers (e.g. ATCG); default=ATCG',default='ATCG')
args = parser.parse_args()