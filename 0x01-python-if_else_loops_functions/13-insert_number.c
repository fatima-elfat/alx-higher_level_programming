#include "lists.h"
/**
* insert_node - inserts a number into a sorted singly linked list.
* @head: head the linked list.
* @number: value of the new node.
* Return: the address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n1, *n2;

	if (!head)
		return (NULL);
	n1 = malloc(sizeof(listint_t));
	if (!n1)
		return (NULL);
	n1->n = number;
	n1->next = NULL;
	if (!*head)
	{
		*head = n1;
		(*head)->next = NULL;
		return (n1);
	}
	n2 = *head;
	while (!n2)
	{
		if (n1->n < n2->n)
		{
			n1->next = n2;
			*head = n1;
			return (n1);
		}
		else if ((n1->n == n2->n) || !n2->next)
		{
			n1->next = n2->next;
			n2->next = n1;
			return (n1);
		}
		n2 = n2->next;
	}
	return (n1);
}
