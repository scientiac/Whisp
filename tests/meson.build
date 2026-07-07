python = import('python').find_installation('python3')

test('Test text_search.py',
  python,
  args: [join_paths(meson.current_source_dir(), 'test_text_search.py')],
  env: ['PYTHONPATH=' + join_paths(meson.project_source_root(), 'src')]
)
