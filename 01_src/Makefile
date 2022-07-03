TEST += test_container.py
TEST += test_items.py
TEST += test_units.py

TEST_LOG = test.log

CMD_TEE = tee -a
.PHONY: test $(TEST)

test: $(TEST) 

$(TEST):
	@rm $(TEST_LOG)
	@echo "#######################################################################" | $(CMD_TEE) $(TEST_LOG)
	@echo "# Test $@ "                                                              | $(CMD_TEE) $(TEST_LOG)
	@echo "#######################################################################" | $(CMD_TEE) $(TEST_LOG)
	
	python $@ | $(CMD_TEE) $(TEST_LOG)

