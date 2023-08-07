#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;

	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		/*if nodes match, cycle found*/
		if (a == b)
			return (1);
	}
	return (0);
}
