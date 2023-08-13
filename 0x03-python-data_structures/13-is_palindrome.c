#include "lists.h"
/**
 * is_palindrome_rec - checks if a sgl linked list is a palindrome recursive.
 * @a: the beginning of list.
 * @z: copy of list, goes to the last node.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome_rec(listint_t **a, listint_t *z)
{
	int r = 0;

	if (z == NULL)
		return (1);
	if (!is_palindrome_rec(a, z->next))
		return (0);
	/* using the poiter for this part*/
	if ((*a)->n == z->n)
		r = 1;
	*a = (*a)->next;
	return (r);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	return (is_palindrome_rec(head, *head));
}
