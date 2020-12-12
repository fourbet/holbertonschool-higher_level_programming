#include "lists.h"

/**
 * sum_dlistint - returns the sum of all the data (n) of a dlistint_t
 *
 * @head: pointer to a dlistint_t
 *
 * Return: the sum
 */

int sum_dlistint(dlistint_t *head)
{
	int sum = 0;
	dlistint_t *current = NULL;

	current = head;
	while (current)
	{
		sum += current->n;
		current = current->next;
	}
	return (sum);
}
