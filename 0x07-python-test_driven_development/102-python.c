#include <stdio.h>
#include "Python.h"

void print_python_string(PyObject *p)
{
	PyASCIIObject *p_clone = (PyASCIIObject *) p;
	Py_ssize_t size;
	wchar_t *s;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	size = p_clone->length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", (long) size);
		printf("  value: %s\n", (char *) (p_clone + 1));
	}
	else
	{
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", (long) size);
		s = PyUnicode_AsWideCharString((PyObject *) p, &size);
		printf("  value: ");
		wprintf(L"%ls\n", s);
		PyMem_Free(s);
	}
}
