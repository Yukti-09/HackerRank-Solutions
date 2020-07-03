struct node *lca( struct node *root, int v1, int v2 ) 
{
    struct node *head=root;
    struct node *head1=root;
    struct node *temp;
    if(v1==root->data || v2==root->data)
    return root;
    while(head!=NULL && head1!=NULL)
    {
        if(head->data==head1->data)
        temp=head1;
        if(head->data>=v1)
        head=head->left;
        else
        head=head->right;
        if(head1->data>=v2)
        head1=head1->left;
        else
        head1=head1->right;
    }
    return temp;
}

