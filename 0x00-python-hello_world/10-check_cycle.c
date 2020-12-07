#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 *@list: pointer to a listin_t
 *
 * Return: 0(no cycle), 1(cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *p = list;
	listint_t *q = list;
	int count = 0;

	while (list)
	{
		if (count != 0 && (p == q))
		{
			return (1);
		}
		count++;
		q = q->next;
		if (p)
		{
			p = p->next;
			if (p)
				p = p->next;
		}
		if (!p && !q)
			return (0);
	}
	return (0);
}
