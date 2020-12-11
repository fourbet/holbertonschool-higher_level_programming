#include "lists.h"

/**
 * dlistint_len - returns the number of elements of a dlistint_t list
 *
 * @h: pointer to distint_t
 *
 * Return: number of nodes
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}
	return (count);
}
