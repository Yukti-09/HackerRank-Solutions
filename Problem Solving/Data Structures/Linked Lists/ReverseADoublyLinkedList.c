DoublyLinkedListNode* reverse(DoublyLinkedListNode* head) 
{
    DoublyLinkedListNode* curr=(DoublyLinkedListNode*)malloc(sizeof(DoublyLinkedListNode));
    DoublyLinkedListNode* temp;
    curr=head;
    temp=NULL;
    if(head->next==NULL)
    {
        return head;
    }
    else
    {
    while(curr!=NULL)
    {
        temp=curr->prev;
        curr->prev=curr->next;
        curr->next=temp;
        curr=curr->prev;
    }
    head=temp->prev;
    }
return head;
}

