bool compare_lists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) 
{
    int flag=0;
    SinglyLinkedListNode* temp=head1;
    SinglyLinkedListNode* temp1=head2;
    while(temp->next!=NULL && temp1->next!=NULL)
    {
        if(temp->data!=temp1->data)
        {
            flag=1;
            break;
        }
        temp=temp->next;
        temp1=temp1->next;
    }
    if(temp->next!=NULL)
    flag=1;
    if(temp1->next!=NULL)
    flag=1;
    if(flag==1)
    return 0; 
    else
    return 1;

}

