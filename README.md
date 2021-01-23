# PyBook

### File structure

* The file name should be something like `myfile.bg`.
* The inner structure of the file is the next:

The first sentence will be always `@META`. This will define the block of metadata that our bookgame contains.

#### @META

| Name | Type | Info              |
| ---- | ---- | ----------------- |
| VEL  | int  | Speed of the text |

`VEL:some_value`

After load the metadata we start to load the cases. Every case start with the line `@CASE` and end with `@END_CASE`. A case could be a node or decision case, or a leaf
or end case, the diference between both is that nodes have the block for `@OPT`.

#### @CASE

| Name | Type | Info              |
| ---- | ---- | ----------------- |
| NUM  | int  | index of the case |

`NUM:case_num`

#### @TEXT

Contains some lines that is the descripction, or narrative of the case.

#### @OP (optional) 

Contains in each line a option for the actual node, if this is a end case this param can be skipped.

Every option use this format:

<character/string>:<description_text>:<next_case(int)>

### BG file example

```
@META
  VEL:10
  
@CASE
  NUM:0
  
  @TEXT
    Here will be three options, choose one.
  
  @OPT
    a:option 1:1
    b:option 2:2
    c:option 3:3
@END_CASE

@CASE
  NUM:1
  @TEXT
    Here there are four options
    First one is recursive.
    Second one, goes to itself.
    Third one goes to next step.
    Forth one goes to the end.
  @OPT
    a:option 1:0
    b:option 2:1
    c:option 3:2
    d:option 4:3
@END_CASE

@CASE
  NUM:2

  @TEXT
    Here is one option
    
  @OPT
    a:option 1:3
@END_CASE

@CASE
  NUM:3
  
  @TEXT
    Final node is here. Bye!
@END_CASE
```
