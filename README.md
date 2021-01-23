# PyBook


#### FILE STRUCT ####

The file name should be <name>.bg 
The inner struc of the file its the next

the first sentence is @META this define the block of metadatas that our bookgame contain
| @META|
| Name | Type |Info|
| ------------- | ------------- | ------------- |
| VEL | int  | Speed of the text |

VEL:<some value>

after load the metadatas we start to load the cases, Every case start with the line @CASE and end with @END_CASE a case could be a node or decision case or a leaf
or end case, the diference between bot is that nodes have the block for @OPT 

| @CASE|
| Name | Type |Info|
| ------------- | ------------- | ------------- |
| NUM | int  | index of the case |

NUM:<case num>

@TEXT contain some lines that is the descripction, or narrative of the case

@OP (optional) Contain in each line a option for the actual node, if this is a end case this param can be obviated.

every option use this format:
<character/string>:<description>:<next_case(int)>
