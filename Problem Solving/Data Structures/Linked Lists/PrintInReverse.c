void reversePrint(SinglyLinkedListNode* head) 
{
    SinglyLinkedListNode* temp=head;
    
    if(temp!=NULL)
    {
        reversePrint(temp->next);
    
        printf("%d\n",temp->data);
    }
    
    
}
