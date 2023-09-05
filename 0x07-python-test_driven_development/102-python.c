#include <stdio.h>
#include "Python.h"

void print_python_string(PyObject *p)
{
	PyASCIIObject *p_clone = (PyASCIIObject *) p;
	wchar_t *buff;
	Py_ssize_t size;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (p_clone->state.ascii == 1)
	{
		printf("  type: compact ascii\n");
	}
	else if (p_clone->state.compact == 1)
	{
		printf("  type: compact unicode object\n");
	}
	else
		printf("  [ERROR] Invalid String Object\n");
	printf("  length: %ld\n", (long) p_clone->length);
	buff = PyUnicode_AsWideCharString(p, &size);
	printf("  value: %ls\n", buff);
	PyMem_Free(buff);
}
