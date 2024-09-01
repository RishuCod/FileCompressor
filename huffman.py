import os
import heapq
class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}
    
    class HeapNode:
        def __init__(self,char,freq):
            self.char=char
            self.freq=freq
            self.left=None
            self.right=None
        def __lt__(self,other):
            return self.freq<other.freq

        def __eq__(self,other):
            if(other==None):
                return False
            if not isinstance(other, HeapNode):
                return False
            return self.freq ==other.freq
          
    def make_frequency_dict(text):
        frequency={}
        for character in text:
            if not character in frequency:
                frequency[character]=0
            frequency[character]+=1
        return frequency 


    def make_heap(self,frequency):
        for key in frequency:
            node=self.HeapNode(key,frequency[key])
            heapq.heappush(self.heap,node)


    def merge_codes(self):
        while(len(len(self.heap)>1)):
            node1=heapq.heappop(self.heap)
            node2=heapq.heappop(self.heap)
            merged=self.HeapNode(None,node1.freq+node2.freq)
            merged.left=node1
            merged.right=node2
            heapq.heappush(self.heap,merged)
    def make_codes_helper(self,node,current_code):
        if(node==None): return
        if(node.char!=None):
            self.codes[node.char]=current_code

        self.make_codes_helper(node.left,current_code+"0")
        self.make_codes_helper(node.right,current_code+"1")
      
    def make_codes(self):
        root=heapq.heappop(self.heap)
        current_code=""
        self.make_codes_helper(root,current_code)


    def get_encode_text(self,text):
        encoded_text=""
        for character in text:
            encoded_text+=self.codes[character]
        return encoded_text
        
    def pad_encoded_text(self,encoded_text):
        extra_padding=8-len(encoded_text)%8
        for _ range(extra_padding):
            encoded_text+="0"
        
        padding_info="{0:08b}".format(extra_padding)
        encoded_text=padding_info+encoded_text
        return encoded_text
    

    def get_byte_array(self,padded_encoded_text):  
        b=bytearray() 
        for i in range(0,len(padded_encoded_text),8):
            byte=padded_encoded_text[i:i+8]
            b.append(int(byte,2)) 

        return b    

    def compress(self):
        filename, file_extension=os.path.splittext(self,path)
        output_path=filename+".bin"    
        with open(self.path,'r') as file, open(output_path,"wb") as output:
            text=file.read()
            text=text.rstrip()
            frequency=make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_codes()
            self.make_codes()
            encoded_text=get_encoded_text(text)
            padded_encoded_text=padded_encoded_text(encoded_text)
            b=self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
        print("compressed")
        return output_path
    
    def decompress(self,input_path):
        filename, file_extension=os.path.splitext(input_path)
        output_path =filename+"_decompressed"+".text"
        with open(input_path,'rb') as file,open(output_path,'w') as output:
            bit_string="
            byte=file.read(1)
            while(len(byte)>0):
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,"0")
                
