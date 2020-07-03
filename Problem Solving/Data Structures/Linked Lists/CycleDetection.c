bool has_cycle(SinglyLinkedListNode* head) 
{
  
    SinglyLinkedListNode* p=(SinglyLinkedListNode*) malloc(sizeof(SinglyLinkedListNode));
    p=head;
    SinglyLinkedListNode* p1=(SinglyLinkedListNode*) malloc(sizeof(SinglyLinkedListNode));
    p1=p->next->next;
    while(p && p1 && p1->next)
    {
        if(p==p1)
        {
            return true;
        }
        p=p->next;
        p1=p1->next->next;
    }
    return false;
}
