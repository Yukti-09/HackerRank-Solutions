DoublyLinkedListNode* sortedInsert(DoublyLinkedListNode* head, int data) 
{
    DoublyLinkedListNode* neww=(DoublyLinkedListNode*)malloc(sizeof(DoublyLinkedListNode));
    DoublyLinkedListNode* temp=(DoublyLinkedListNode*)malloc(sizeof(DoublyLinkedListNode));
    
    temp=head;
    neww->data=data;
    neww->prev=NULL;
    neww->next=NULL;
    if(head==NULL)
    {
        head=neww;
        
    }
    else if(neww->data<temp->data)
    {
            neww->next=temp;
            temp->prev=neww;
            head=neww;
    }
    else 
        {
            
            while(temp->next!=NULL && temp->next->data < neww->data)
            {
                temp=temp->next;
            }
                if(temp->next!=NULL)
                {
                    temp->next->prev=neww;
                    neww->next=temp->next;
                    temp->next=neww;
                    neww->prev=temp;
                }
                else 
                {
                    temp->next=neww;
                    neww->prev=temp;
                }
            }

return head;
 }
